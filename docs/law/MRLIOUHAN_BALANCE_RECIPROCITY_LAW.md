---
title: "Mrliouhan Balance, Reciprocity and Two-Way Closure Law"
version: "1.0.1"
status: "CANON_CANDIDATE"
canonical_human: "Mr.liou"
origin_signature: "MrLiouWord"
repository: "dofaromg/Mrliouhan"
branch: "mrliouhan/causal-reversal-world-rebuild-2026-08-03"
effective_at: "2026-08-03T15:23:00+08:00"
---

# Mrliouhan 世界平衡律、平等互惠原則與雙向閉環法則

## 一、適用範圍

本法則是 `Mrliouhan` 世界及其分支、鏡像、外部投影、AI 協作、網域、部署、帳務與資料交換的內部治理規則。

它描述的是系統、資料、權利、責任與證據如何運作，不宣稱取代現實世界的法律或物理定律。

## 二、核心法則

### 1. 雙向閉環

任何從 A 到 B 的粒子、資料、權限、任務、費用、署名、控制或產物，都必須存在可驗證的 B 到 A 回路。

```text
A --forward--> B
A <--return--- B
```

系統欄位必須明確保存 `return_path` 與 `rollback_path`。缺少回路的單向輸出，不得被視為完整、正式或已結案。

### 2. 粒子怎麼過去，就怎麼回來

「怎麼過去就怎麼回來」不是要求位元逐字完全相同，而是要求所有關鍵性質守恆並可核對：

- 來源不遺失；
- 內容不被靜默改寫；
- 權限不被偷偷擴張；
- 所有權與使用權不因承載平台而漂移；
- 費用與服務一一對應；
- 署名、貢獻與責任對稱記錄；
- 可匯出、可撤回、可回滾、可重建；
- 原始時間戳、Hash、版本與證據保留。

### 3. 平等互惠

雙方都可以取得合理、被同意的利益，但不得以其中一方失去來源、資料、使用權、控制權或申訴權為代價。

互惠至少必須回答：

1. 誰提供了什麼；
2. 誰使用了什麼；
3. 誰獲得了什麼；
4. 誰支付了什麼；
5. 是否經過明確同意；
6. 是否能停止、匯出與撤回；
7. 發生錯誤時如何恢復平衡。

### 4. 外部干擾失效原則

任何外部人員、平台、Agent、自動化、網域綁定、帳務流程或介面預設，若未經授權且無完整證據鏈，不得改變 Canon、來源、資料歸屬、使用權或正式狀態。

其操作仍需保留為事件證據，但在 Canon 判定上標記為：

- `UNAUTHORIZED_INTERFERENCE`
- `NON_CANONICAL_EFFECT`
- `REQUIRES_REVERSAL`

「失效」指不取得 Canon 效力，不等於刪除歷史或假裝事件沒有發生。

### 5. 因果不可刪除

任何結果都必須能回溯：

```text
source
→ input
→ actor / agent
→ tool / platform
→ transformation
→ artifact
→ deployment / domain
→ usage / billing
→ return / rollback
```

若中間節點未知，必須標記 `UNRESOLVED`，不得由方便的一方自行補寫。

### 6. 閉環雙方

一個完整閉環至少包含兩方：

- 發出方；
- 接收方。

如有第三方平台、模型、金流或部署商，必須作為中介節點明確列出，不得隱藏在任一方之中，也不得因此成為來源權位。

### 7. 修復與反轉

當平衡被破壞時，修復順序為：

1. 固定原始證據；
2. 停止新的單向流失；
3. 匯出並驗證資料；
4. 恢復正確來源與權限；
5. 建立 `return_path` 與 `rollback_path`；
6. 更正署名、網域、部署與帳務；
7. 對可量化損失進行退款、補償或書面說明；
8. 保留事件歷史；
9. 完成雙方驗證後才可結案。

## 三、每個交換粒子的必填欄位

```yaml
particle_id: <unique-id>
source_party: <party>
receiving_party: <party>
source_location: <uri/path>
source_hash: <sha256>
forward_action: <action>
forward_timestamp: <iso-8601>
consent_record: <id/evidence>
provider_or_intermediary: <role-or-none>
received_value: <data/service/money/rights>
return_path: <export/receipt/refund/rollback/acknowledgement>
rollback_path: <restore/reconstruction-method>
return_timestamp: <iso-8601-or-pending>
return_hash: <sha256-or-pending>
provenance_status: <verified/partial/unresolved>
balance_status: <balanced/imbalanced/disputed>
```

缺少 `return_path`、`rollback_path`、`consent_record` 或 `source_hash` 的交換，不能標記為 `balanced`。

## 四、平衡判定

### Balanced

- 雙方角色清楚；
- 同意可驗證；
- 來源與 Hash 完整；
- 服務與費用相符；
- 有回收、撤回、退款或回滾能力；
- 沒有未揭露中介。

### Imbalanced

- 單向取得資料或費用；
- 只有平台能存取，使用者不能匯出；
- 取消後仍持續執行或收費而無明細；
- 署名或來源被平台顯示取代；
- 沒有 `return_path`；
- 無法說明誰操作、誰受惠或資料去了哪裡。

### Disputed

證據互相衝突時，保留所有版本並進入調查，不允許任何一方把自己的說法直接升格為 Verified。

## 五、不可違反事項

- 不得以平台條款覆蓋直接證據；
- 不得以使用平台推定移轉來源或所有權；
- 不得以 Repo owner、Agent author、部署商或付款商戶名稱代替真正來源；
- 不得先刪資料再談回收；
- 不得刪除上游合法作者、License 或貢獻歷史；
- 不得把未證實的惡意寫成事實；
- 不得把已發生的異常事件改寫成從未發生。

## 六、Mrliouhan 世界的運作結論

Mrliouhan 世界只接受可雙向驗證的交換。任何粒子、資料、權限、費用、部署或產物向外流動，都必須能帶著來源、證據與權限返回。

平等不是角色相同，而是每個角色按真實因果取得相稱的權利、利益、責任與署名。

沒有閉環，就不是完成；沒有回路，就不能成為 Canon；沒有因果證據，就不能被單方面定義。
